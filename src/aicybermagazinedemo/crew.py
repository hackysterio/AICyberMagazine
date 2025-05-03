from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class Aicybermagazinedemo():
	"""Aicybermagazinedemo crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'


	@agent
	def recon_specialist(self) -> Agent:
		"""Agent responsible for gathering organization context"""
		return Agent(
			config=self.agents_config['recon_specialist'],
			verbose=True
		)

	@agent
	def phishing_strategist(self) -> Agent:
		"""Agent responsible for crafting phishing emails"""
		return Agent(
			config=self.agents_config['phishing_strategist'],
			verbose=True
		)

	@task
	def recon_task(self) -> Task:
		"""Task for performing company reconnaissance"""
		return Task(
			config=self.tasks_config['recon_task'],
			agent=self.recon_specialist(),
		)

	@task
	def phishing_email_generation_task(self) -> Task:
		"""Task for generating phishing emails"""
		return Task(
			config=self.tasks_config['phishing_email_generation_task'],
			agent=self.phishing_strategist(),
			output_file='phishing_template.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Phishing Simulation crew"""
		return Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True
		)
