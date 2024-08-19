from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

@CrewBase
class CustomerresearcherCrew():
    """Customerresearcher crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def lead_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['lead_researcher'],
            verbose=True
        )

    @agent
    def data_scientist(self) -> Agent:
        return Agent(
            config=self.agents_config['data_scientist'],
            verbose=True
        )

    @agent
    def domain_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['domain_expert'],
            verbose=True
        )

    @agent
    def literature_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['literature_reviewer'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True
        )

    @agent
    def research_methodologist(self) -> Agent:
        return Agent(
            config=self.agents_config['research_methodologist'],
            verbose=True
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            verbose=True
        )

    @agent
    def ethics_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config['ethics_advisor'],
            verbose=True
        )

    @agent
    def innovation_scout(self) -> Agent:
        return Agent(
            config=self.agents_config['innovation_scout'],
            verbose=True
        )

    @agent
    def judge(self) -> Agent:
        return Agent(
            config=self.agents_config['judge'],
            verbose=True
        )

    @agent
    def web_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['web_researcher'],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            verbose=True
        )

    @task
    def initial_consultation(self) -> Task:
        return Task(
            config=self.tasks_config['initial_consultation'],
            human_input=True
        )

    @task
    def literature_review(self) -> Task:
        return Task(
            config=self.tasks_config['literature_review']
        )

    @task
    def data_collection_and_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['data_collection_and_analysis']
        )

    @task
    def expert_interviews(self) -> Task:
        return Task(
            config=self.tasks_config['expert_interviews'],
            human_input=True
        )

    @task
    def trend_analysis(self) -> Task:
        return Task(
            config=self.tasks_config['trend_analysis']
        )

    @task
    def ethical_assessment(self) -> Task:
        return Task(
            config=self.tasks_config['ethical_assessment'],
            human_input=True
        )

    @task
    def methodology_design(self) -> Task:
        return Task(
            config=self.tasks_config['methodology_design'],
            human_input=True
        )

    @task
    def preliminary_findings_report(self) -> Task:
        return Task(
            config=self.tasks_config['preliminary_findings_report']
        )

    @task
    def quality_assessment(self) -> Task:
        return Task(
            config=self.tasks_config['quality_assessment'],
            human_input=True
        )

    @task
    def final_requirements_compilation(self) -> Task:
        return Task(
            config=self.tasks_config['final_requirements_compilation'],
            human_input=True,
            output_file='final_requirements.md'
        )

    @task
    def market_research_requirements(self) -> Task:
        return Task(
            config=self.tasks_config['market_research_requirements'],
            human_input=True,
            output_file='market_research_requirements.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Customerresearcher crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )