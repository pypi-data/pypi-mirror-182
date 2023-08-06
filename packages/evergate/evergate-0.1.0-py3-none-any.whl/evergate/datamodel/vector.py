"""
"""


from pydantic import BaseModel, Field


class Vector3d(BaseModel):
  """A data model for a 3d vector.

  Attributes:
    x (float): The x coordinate.
    y (float): The y coordinate.
    z (float): The z coordinate.
  """

  x: float = Field(description="The x coordinate.")
  y: float = Field(description="The y coordinate.")
  z: float = Field(description="The z coordinate.")
