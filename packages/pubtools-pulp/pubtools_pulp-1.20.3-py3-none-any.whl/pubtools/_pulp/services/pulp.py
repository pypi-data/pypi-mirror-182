import threading
import os
import sys
import logging
import warnings

from pubtools import pulplib

from .base import Service
from .fakepulp import new_fake_controller

LOG = logging.getLogger("pubtools.pulp")


def pulp_throttle(str_pulp_throttle):
    val = int(str_pulp_throttle)
    if val <= 0:
        raise ValueError
    return val


# Because class is designed as a mix-in...
# pylint: disable=no-member


class PulpClientService(Service):
    """A service providing a Pulp client.

    If this service is inherited, Pulp-related arguments become mandatory
    in order to run the task.
    """

    def __init__(self, *args, **kwargs):
        self.__lock = threading.RLock()
        self.__instance = None
        self.__fake_controller = None
        super(PulpClientService, self).__init__(*args, **kwargs)

    def add_service_args(self, parser):
        super(PulpClientService, self).add_service_args(parser)

        group = parser.add_argument_group("Pulp environment")
        group.add_argument("--pulp-url", help="Pulp server URL")
        group.add_argument("--pulp-user", help="Pulp username", default=None)
        group.add_argument(
            "--pulp-password",
            help="Pulp password (or set PULP_PASSWORD environment variable)",
            default=None,
        )
        group.add_argument(
            "--pulp-insecure",
            action="store_true",
            help="Allow unverified HTTPS connection to Pulp",
        )
        group.add_argument(
            "--pulp-throttle",
            help="Allows to enqueue or run only specified number of Pulp tasks at one moment "
            + "(or set PULP_THROTTLE environment variable)",
            default=None,
            type=pulp_throttle,
        )
        group.add_argument(
            "--pulp-fake",
            help=(
                "Use a fake in-memory Pulp client rather than interacting with a real server. "
                + "For development/testing only, may have limited functionality."
            ),
            action="store_true",
        )

    @property
    def pulp_client(self):
        """A shared Pulp client used during task, instantiated on demand."""
        with self.__lock:
            if not self.__instance:
                self.__instance = self.new_pulp_client()
                self.__instance.__enter__()
        return self.__instance

    @property
    def pulp_fake_controller(self):
        """A Pulp fake controller used during task, instantiated on demand."""
        with self.__lock:
            if not self.__fake_controller:
                self.__fake_controller = new_fake_controller()
        return self.__fake_controller

    def new_pulp_client(self, **kwargs):
        """Creates and returns a new Pulp client with appropriate config."""
        auth = None
        args = self._service_args

        if not args.pulp_fake and not args.pulp_url:
            LOG.error("At least one of --pulp-url or --pulp-fake must be provided")
            sys.exit(41)

        if args.pulp_fake:
            LOG.warning("Using a fake Pulp client, no changes will be made to Pulp!")
            return self.pulp_fake_controller.new_client()

        # checks if pulp password is available as environment variable
        if args.pulp_user:
            pulp_password = args.pulp_password or os.environ.get("PULP_PASSWORD")
            if not pulp_password:
                LOG.warning("No pulp password provided for %s", args.pulp_user)
            auth = (args.pulp_user, pulp_password)

        kwargs = kwargs.copy()
        kwargs["auth"] = auth

        if args.pulp_insecure:
            kwargs["verify"] = False

            # Thank you, but we don't need to hear about this for every single request
            warnings.filterwarnings("once", r"Unverified HTTPS request is being made")

        if args.pulp_throttle or os.environ.get("PULP_THROTTLE"):
            kwargs["task_throttle"] = args.pulp_throttle or pulp_throttle(
                os.environ.get("PULP_THROTTLE")
            )

        return pulplib.Client(args.pulp_url, **kwargs)

    def __exit__(self, *exc_details):
        if self.__instance:
            self.__instance.__exit__(*exc_details)

        super(PulpClientService, self).__exit__(*exc_details)
