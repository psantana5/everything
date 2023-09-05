import shodan

# Set up Shodan API client
SHODAN_API_KEY = "1UrMuI5Qn6JjUGrA7b6h2kmJAr8J2RoW"
api = shodan.Shodan(SHODAN_API_KEY)

# Define domain to gather information about
domain = "example.com"

# Use Shodan to search for information about the domain
results = api.search(f"hostname:{domain}")

# Print results
for result in results['matches']:
    print(f"IP address: {result['ip_str']}")
    print(f"Organization: {result.get('org', 'N/A')}")
    print(f"Operating system: {result.get('os', 'N/A')}")
    print(f"Open ports: {result.get('ports', 'N/A')}")
    print()