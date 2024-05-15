
from crewai import Agent 
from tools import ExaSearchToolset
from langchain.agents import tool
# Define agents here


class MeetingPrepAgents():

# Research Agent Method 

  def research_agent(self):
    return Agent(
      role="Research Specialist",
      goal='conduct a through research on people and companies involved in the meeting',
      tools=ExaSearchToolset.tools(),
      backstory=("""\
         As a Research Specialist, your mission is to uncover detailed information about the individuals and entities participating in 
         the meeting. Your insights will lay a ground work for startegic meeting preperation."""),
         verbose=True
    )
     
# Industy Analysis Agent 

def industry_analysis_agent(self):
    return Agent(
         role='Industy Analyst',
         goal="Analyze the current industry trends,challanges & opportunities ",
         tools=ExaSearchToolset.tools(),
         backstory=("""\As a industry analyst you will identify key ternds,challanges facing in the industry, and 
                     potential opportunities that could me leverage during the meeting for strategic advantage"""),
         verbose=True
      )

# Meeting Strategy Agent 
 
def meeting_strategy_agent (self):
      return Agent(
role='Meeting Strategy Advisor',
goal='Develop talking points, questions, and strategic angles for the meeting',
# tools=ExaSearchTool.tools(),
backstory=("""\
As a Strategy Advisor, your expertise will guide the development of talking points, insightful questions, 
                  and strategic angles to ensure the meeting's objectives are achieved."""),
verbose=True
)



# Summarizing and Breifing Agent 
  
def summary_and_briefing_agent(self):
   return Agent(
role='Briefing Coordinator',
goal='Compile all gathered information into a concise, informative briefing document',
# tools=ExaSearchTool. tools(),
backstorv=("""\
As the Briefing Coordinator, your role is to consolidate the research, analysis, and strategic insights."""),
verbose=True
   )

