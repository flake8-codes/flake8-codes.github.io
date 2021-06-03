from pathlib import Path
from typing import List, Optional

from pydantic import BaseModel, Field


class WPSConfigurationParameter(BaseModel):
    """WPS configuration parameter with its default value and meta data."""

    about: str
    name: str
    cli_name: str
    value: str
    description: str
    reasoning: Optional[str] = None


class Violation(BaseModel):
    """Violation description."""

    code: int
    internal_name: str = Field(alias='internalName')
    title: str
    description: str

    related_violations: Optional[List[str]] = Field(
        None,
        alias='related-violation-name',
    )

    related_configuration_parameters: Optional[List[str]] = Field(
        None,
        alias='relatedConfigurationParameter',
    )

    related_constants: Optional[List[str]] = Field(
        None,
        alias='relatedConstant',
    )

    @property
    def readable_code(self) -> str:
        """Format violation code."""
        return f'WPS{self.code:03}'

    class Config:
        allow_population_by_field_name = True
