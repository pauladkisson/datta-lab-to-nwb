"""Primary class for handling velocity-trigger information from velocity-modulation experiments."""
from neuroconv.basedatainterface import BaseDataInterface
from neuroconv.utils import load_dict_from_file
from pynwb import NWBFile
from .metadatainterface import MetadataInterface


class VelocityTriggerInterface(MetadataInterface):
    """Velocity trigger interface for markowitz_gillis_nature_2023 conversion"""

    def get_metadata(self) -> dict:
        metadata = super().get_metadata()
        session_metadata = load_dict_from_file(self.source_data["session_metadata_path"])
        session_metadata = session_metadata[self.source_data["session_uuid"]]

        metadata["VelocityModulation"]["trigger_syllable"] = session_metadata["trigger_syllable"]
        metadata["VelocityModulation"]["threshold"] = session_metadata["trigger_syllable_scalar_threshold"]
        metadata["VelocityModulation"]["comparison"] = session_metadata["trigger_syllable_scalar_comparison"]

        return metadata

    def get_metadata_schema(self) -> dict:
        metadata_schema = super().get_metadata_schema()
        metadata_schema["properties"]["VelocityModulation"] = {
            "type": "object",
            "properties": {
                "trigger_syllable": {"type": "number"},
                "threshold": {"type": "string"},
                "comparison": {"type": "string"},
            },
        }
        return metadata_schema
