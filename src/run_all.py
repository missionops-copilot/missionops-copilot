import logging
import sys

# Ensure basic logging is configured
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    """
    Week 1 stub.
    Tech debt: replace with argparse CLI + logging module + sys.exit(1) on failure before Week 3.
    """
    print("MissionOps Copilot: run_all execution")
    
    success = True

    # Aircraft Module (Placeholder)
    try:
        print("--- Running Aircraft Module ---")
        # TODO: run aircraft module
        print("Aircraft module placeholder complete.")
    except Exception as e:
        logger.error(f"Aircraft module failed: {e}")
        success = False

    # Spacecraft Module (Minimal PR #1 Stub)
    try:
        print("--- Running Spacecraft Module ---")
        print("spacecraft: ok")
    except Exception as e:
        logger.error(f"Spacecraft module failed: {e}")
        success = False

    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
