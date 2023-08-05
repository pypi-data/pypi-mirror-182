import dataclasses
import logging
import re
from typing import Dict, Optional, Tuple, TypeVar, Generic, List, Union

from qm.octave import OctaveOutput, OctaveLOSource
from qm.octave.calibration_db import CalibrationDB


logger = logging.getLogger(__name__)

ConnectionMapping = Dict[Tuple[str, int], Tuple[str, str]]

DEFAULT_CONNECTIONS = {
    1: "I1",
    2: "Q1",
    3: "I2",
    4: "Q2",
    5: "I3",
    6: "Q3",
    7: "I4",
    8: "Q4",
    9: "I5",
    10: "Q5",
}


@dataclasses.dataclass
class ConnectionInfo:
    host: str
    port: int

    def __hash__(self):
        return hash((self.host, self.port))


PortType = TypeVar("PortType", OctaveOutput, OctaveLOSource)


@dataclasses.dataclass
class LoopbackInfo(Generic[PortType]):
    name: str
    octave_port: PortType

    def __hash__(self):
        return hash((self.name, self.octave_port))


def _convert_octave_port_to_number(port: str) -> int:
    if port == "I1":
        return 1
    elif port == "Q1":
        return 1
    elif port == "I2":
        return 2
    elif port == "Q2":
        return 2
    elif port == "I3":
        return 3
    elif port == "Q3":
        return 3
    elif port == "I4":
        return 4
    elif port == "Q4":
        return 4
    elif port == "I5":
        return 5
    elif port == "Q5":
        return 5


def _convert_number_to_octave_port(name: str, port: int) -> List:
    return [(name, f"I{port}"), (name, f"Q{port}")]


class QmOctaveConfig:
    def __init__(self, **kwargs):
        self._devices: Dict[str, ConnectionInfo] = {}
        self._calibration_db_path: Optional[str] = None
        self._loopbacks: Dict[
            LoopbackInfo[OctaveLOSource], LoopbackInfo[OctaveOutput]
        ] = {}
        self._opx_octave_port_mapping: ConnectionMapping = {}
        self._calibration_db: Optional[CalibrationDB] = None
        self._fan = None
        if "fan" in kwargs:
            self._fan = kwargs.get("fan")

    @property
    def fan(self):
        return self._fan

    def add_device_info(self, name: str, host: str, port: int):
        """
        Sets the octave info  - the IP address can be either the router ip or the actual ip
        depends on the installation configuration (cluster or standalone mode)

        :param name: str
        :param host: str
        :param port: int
        """
        # can be either the router ip or the actual ip (depends on what we have)
        self._devices[name] = ConnectionInfo(host, port)

    def get_devices(self) -> Dict[str, ConnectionInfo]:
        return self._devices

    def set_calibration_db(self, path):
        """
        Sets the path to the calibration DB

        :param path: str
        """
        self._calibration_db_path = path

    @staticmethod
    def _check_connection_format(connection: Tuple[str, Union[int, str]]) -> bool:
        return (
            isinstance(connection, tuple)
            and len(connection) == 2
            and isinstance(connection[0], str)
        )

    def set_opx_octave_mapping(self, mappings: List[Tuple[str, str]]):
        """
        Sets the default port mapping for each `opx, octave` names
        """
        if self._opx_octave_port_mapping:
            logger.warning(
                "Setting opx-octave default port mapping, "
                "your configured mapping will be overridden!"
            )

        for opx_name, octave_name in mappings:
            self._opx_octave_port_mapping.update(
                self.get_default_opx_octave_port_mapping(opx_name, octave_name)
            )

    def add_opx_octave_port_mapping(self, connections: ConnectionMapping):
        """
        Adds port mapping which is different than the default one. should be in the form:
        Dict[Tuple["con1", 1], Tuple["octave1", "I1"]
        ...
        ...
        ]

        :param connections: ConnectionMapping
        """
        # ("con1", 1): ("octave1", "I1")
        # validate structure:
        for opx_connection, octave_connection in connections.items():
            if not (
                self._check_connection_format(opx_connection)
                and isinstance(opx_connection[1], int)
            ):
                raise ValueError(
                    f"key {opx_connection} is not according to format "
                    f'("con_name", "port_index")'
                )
            pattern = re.compile("([IQ])([12345])")
            if not (
                self._check_connection_format(octave_connection)
                and isinstance(octave_connection[1], str)
                and pattern.match(octave_connection[1]) is not None
            ):
                raise ValueError(
                    f"value {octave_connection} is not according to format "
                    f'("octave_name", "octave_port")'
                )

        self._opx_octave_port_mapping.update(connections)

    def get_opx_octave_port_mapping(self) -> ConnectionMapping:
        """
        Get the configured opx-octave connections
        """
        if self._opx_octave_port_mapping:
            return self._opx_octave_port_mapping
        else:
            raise RuntimeError(
                "No opx-octave mapping available, "
                "please run 'set_opx_octave_mapping' or "
                "'add_opx_octave_port_mapping' "
                "before attempting to read them."
            )

    @staticmethod
    def get_default_opx_octave_port_mapping(
        controller_name: str, octave_name: str
    ) -> ConnectionMapping:
        """
        Get the default opx-octave connections
        """
        default_connections = {}
        for opx_port, octave_port in DEFAULT_CONNECTIONS.items():
            default_connections[(controller_name, opx_port)] = (
                octave_name,
                octave_port,
            )
        return default_connections

    @property
    def calibration_db(self) -> CalibrationDB:
        if (
            self._calibration_db is None
            or self._calibration_db_path == self._calibration_db.file_path
        ) and self._calibration_db_path is not None:
            self._calibration_db = CalibrationDB(self._calibration_db_path)
        return self._calibration_db

    def add_lo_loopback(
        self,
        octave_output_name: str,
        octave_output_port: OctaveOutput,
        octave_input_name: str,
        octave_input_port: OctaveLOSource,
    ):
        """
        Adds a loopback between an OctaveOutput and an OctaveLOSource
        """

        if octave_output_name != octave_input_name:
            raise ValueError(
                "lo loopback between different octave devices are not supported"
            )
        loop_back_source = LoopbackInfo(octave_output_name, octave_output_port)
        loop_back_destination = LoopbackInfo(octave_input_name, octave_input_port)
        self._loopbacks[loop_back_destination] = loop_back_source

    def get_lo_loopbacks_by_octave(
        self, octave_name: str
    ) -> Dict[OctaveLOSource, OctaveOutput]:
        """
        Gets a list of all loop backs by octave name
        """

        result = {}
        for destination, source in self._loopbacks.items():
            if destination.name == octave_name:
                result[destination.octave_port] = source.octave_port
        return result

    def get_opx_iq_ports(self, octave_output_port: Tuple[str, int]):
        conns = self.get_opx_octave_port_mapping()
        inv_conns = {v: k for k, v in conns.items()}
        octave_input_port_i, octave_input_port_q = _convert_number_to_octave_port(
            octave_output_port[0], octave_output_port[1]
        )
        if octave_input_port_i not in inv_conns:
            octave_name, octave_port = octave_input_port_i
            raise KeyError(
                f"Could not find opx connections to port "
                f"'{octave_port}' of octave '{octave_name}'"
            )

        if octave_input_port_q not in inv_conns:
            octave_name, octave_port = octave_input_port_q
            raise KeyError(
                f"Could not find opx connections to port "
                f"'{octave_port}' of octave '{octave_name}'"
            )
        return [inv_conns[octave_input_port_i], inv_conns[octave_input_port_q]]
