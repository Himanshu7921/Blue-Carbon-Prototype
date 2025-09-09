from blockchain import add_block, view_chain, issue_tokens, tokens

num_projects = int(input("How many projects do you want to add? "))

for _ in range(num_projects):
    project_name = input("Enter project name: ")
    user = input("Enter NGO/Community name: ")
    trees = int(input("Enter number of trees planted: "))
    gps = input("Enter GPS coordinates (lat,long): ")
    photo_url = input("Enter photo URL: ")

    # Create project dictionary
    project_data = {
        "project_name": project_name,
        "user": user,
        "trees": trees,
        "gps": gps,
        "photo_url": photo_url
    }

    # Verification step
    verify = input("Verify this project? (yes/no): ").strip().lower()
    verified = verify == "yes"

    # Add block with verification status
    block = add_block(project_data, verified)
    print(f"\nBlock added for project: {project_name}")

    # Issue tokens only if verified
    if verified:
        issue_tokens(user, trees)
    else:
        print(f"Project {project_name} not verified. No tokens issued.\n")

# Print current token balances
print("\n--- Current Token Balances ---")
for user, balance in tokens.items():
    print(f"{user}: {balance} tokens")

# Print blockchain summary
print("\n--- Blockchain Summary ---")
view_chain()