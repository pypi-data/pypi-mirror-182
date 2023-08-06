import subprocess

class EnvGenerator():

	def create(self, project_name: str):
		try:
			process = subprocess.Popen(['python', '-m', 'venv', f"{project_name}/env"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			stdout, stderr = process.communicate()
			if stderr:
				print(f"Error generating virtual env: {stderr}")
		except Exception as e:
			print(f"Error generating virtual env: {e}")