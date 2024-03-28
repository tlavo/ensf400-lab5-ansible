import ansible_runner

def load_inventory():
    r = ansible_runner.interface.run(
        private_data_dir='./',
        host_pattern='all',
        playbook='inventory.yml',
        inventory='./hosts.yml',
        private_key_file='./secrets/id_rsa',
        host_key_checking=False,
        action_warnings=False
    )

    # Check if the execution was successful
    if r.status == "successful":
        for event in r.events:
            print(event['stdout'])
    else:
        print("Inventory loading failed.")

def main():
    load_inventory()

if __name__ == "__main__":
    main()
