from dotenv import load_dotenv

def Load_env() -> bool:
	return load_dotenv(
		dotenv_path = './Backend/.env',
		encoding = 'utf-8',
		override = True,
		verbose = True
	)