from parsers.resume_parser import parse_resume
from ats_engine.ats_scorer import calculate_ats_score
from screening_ai.screening_logic import screening_decision
from scoring.score_aggregator import aggregate_score
from utils.logger import setup_logger


def main():
    logger = setup_logger()
    logger.info("Zecpath AI System Started")

    print("📄 Reading Resume...")
    resume_text = parse_resume("data/sample_resume.txt")

    print("🧠 Calculating ATS Score...")
    ats_score = calculate_ats_score(resume_text)

    print("📊 Making Screening Decision...")
    decision = screening_decision(ats_score)

    print("🔢 Aggregating Final Score...")
    final_score = aggregate_score(ats_score)

    logger.info(f"ATS Score: {ats_score}")
    logger.info(f"Final Score: {final_score}")
    logger.info(f"Decision: {decision}")

    print("\n===== RESULT =====")
    print("ATS Score:", ats_score)
    print("Final Score:", final_score)
    print("Screening Decision:", decision)


if __name__ == "__main__":
    main()
