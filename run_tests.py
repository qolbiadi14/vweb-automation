import sys
from behave import __main__ as behave_main

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python run_tests.py <feature_file> <subdomain> <username> <password>")
        sys.exit(1)
    
    feature_file = sys.argv[1]
    subdomain = sys.argv[2]
    username = sys.argv[3]
    password = sys.argv[4]
    
    behave_args = [
        feature_file,
        "-D", f"subdomain={subdomain}",
        "-D", f"username={username}",
        "-D", f"password={password}",
        "--no-capture",
        "--no-capture-stderr"
    ]
    behave_main.main(args=behave_args)