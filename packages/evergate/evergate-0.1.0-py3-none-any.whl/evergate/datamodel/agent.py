"""
"""

from datetime import datetime
from pydantic import BaseModel, Field


class AgentResearch(BaseModel):
  """
  """

  agent_id: int = Field(
      description="An id of the agent who offers this research.")
  points_per_day: float = Field(
      description="The amounts of research points granted per day.")
  remainder_points: float = Field(
      description="The remaining research points to complete.")
  skill_type_id: int = Field(
      description="An id of the skill that is being researched.")
  started_at: datetime = Field(
      description="The datetime when this research was started.")
