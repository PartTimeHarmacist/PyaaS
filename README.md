# PyaaS
Python As A Service - Distributed Python Fragments


### So, what is this thing?
This is a project which aims to support python functions as a service, that can be deployed via
docker compose or docker swarm.  Kubernetes support probably isn't too far behind after that.

The main purpose of this project is to provide a quick and simple way to deploy and schedule arbitrary 
python code fragments, *without* tying everything to the host system.


### How will it work?
The basic idea is that you provide a code snippet or file to the platform, tell it what schedule to run on,
 and it will take care of the rest!  It'll deploy the code via docker images, based on the `python:slim` 
image by default.  The cron job will be scheduled inside the container, and run until a specified end date,
or until stopped.


### Valid Schedules
Any valid cron schedule will be accepted.  See https://crontab.guru/ for assistance with cron schedules.
#### Special Schedules
| Schedule | Definition | Equivalent Cron Schedule |
| --- | --- | --- |
| `@once` or `@now` | Run once and only once. | `N/A` |
| `@inf` | Run continually, restarting each time the script completes, regardless of success. | `N/A` |
| `@daily` | Run daily at midnight. | `0 0 * * *` |
| `@hourly` | Run every hour at minute 0 (eg 08:00, 09:00, etc) | `0 * * * * ` |
| `@monthly` | Run the first day of each month at 00:00 | `0 0 1 * *` |
| `@yearly` | Run the first day of January each year, at 00:00 | `0 0 1 1 *` |
| `@none` or `None` | Do not run the code, only deploy it.  This code will only be run via manual trigger. | `N/A` |


### Goals of PyaaS
- [ ] Deployments
    - [ ] Support deployment of individual, no-file function snippets
    - [ ] Support deployment of complete packages and/or projects
    - [ ] Support deployment of projects via git links
    - [ ] Support automatic update checking of projects tied to git repos
- [ ] User Experience
    - [ ] Intuitive CLI
        - [ ] Follow systemctl/kubectl patterns
        - [ ] Full command completion support 
    - [ ] Web Based UI
        - [ ] Monitor deployments at a glance
        - [ ] Deploy from web UI via upload or direct coding
        - [ ] Full Schedule view with calendar like interface
        - [ ] Cronjob schedule visualizer
        - [ ] Authentication
            - [ ] Username/Password
            - [ ] Master Password/Passphrase
            - [ ] 2Factor Key/YubiKey
            - [ ] LDAP
            - [ ] OAuth/OpenID
            - [ ] Windows/Azure