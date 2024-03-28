import ansible_runner

def run_playbook():
    r = ansible_runner.interface.run(
        private_data_dir='./',
        playbook='hello.yml',
        inventory='./hosts.yml',
        host_pattern='app_group',
        private_key_file='./secrets/id_rsa',
        host_key_checking=False,
        action_warnings=False
    )

    # Check if the execution was successful
    if r.status == "successful":
        for event in r.events:
            print(event['stdout'])
    else:
        print("Playbook execution failed.")

def main():
    run_playbook()

if __name__ == "__main__":
    main()
