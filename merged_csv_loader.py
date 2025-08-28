# 社員名簿CSVを1ドキュメントとして読み込むローダー
import pandas as pd
from langchain_core.documents import Document

def load_merged_employee_csv(csv_path: str) -> list:
	"""
	社員名簿CSVを全行まとめて1つのドキュメントとして読み込む。
	各従業員の情報は1人1ブロックとしてテキスト化し、全員分を連結する。
	検索精度向上のため、各項目名を明示し、改行区切りで整形する。
	"""
	df = pd.read_csv(csv_path)
	# 各従業員の情報を1人1ブロックのテキストに整形
	people = []
	for _, row in df.iterrows():
		person = []
		for col in df.columns:
			person.append(f"{col}: {row[col]}")
		people.append("\n".join(person))
	# 全員分を2行改行で連結
	all_text = "\n\n".join(people)
	# LangChainのDocumentとして返す
	return [Document(page_content=all_text, metadata={"source": csv_path})]
