op_timeout = 2

hosts = [
    {
        "hostname": "futex.cd80.net",
        "services": [
            {
                "name": "ssh",
                "type": "ssh",
                "port": 22,
                "key": "AAAAB3NzaC1yc2EAAAADAQABAAABAQC7h5kglsdNa6wfoKP/ZHOMtNgFICRxvCIepgR33yrGFP9Ij34b1G2O/1A7DbMCOM9Us6SmUwWUq7ARFLEoeLOyPKpNS0PH1Lau9F20dRI59A2gnLI2AwiYC3AqYwBl6wkG1jDps8Q5o614keeyaLdr7Ks9r45d20qZm87x2wt+sncHP3Y/lsnLis3iS1hnhGCZC0qMdW011F0vuKuLE4KPKOCdjywAcpLlE48eAe9/uMLhdZreN/E3yHISzxLxQNWR7ywycoN1RrRiX5983e+sUL0z0PaqxMptsxncT1Rcpx9CziPF76fKKggt5LsHH9JskQ1XhonifWK9Si5NY1at"
            },
            {
                "name": "ssh (alternative port)",
                "type": "ssh",
                "port": 443,
                "key": "AAAAB3NzaC1yc2EAAAADAQABAAABAQC7h5kglsdNa6wfoKP/ZHOMtNgFICRxvCIepgR33yrGFP9Ij34b1G2O/1A7DbMCOM9Us6SmUwWUq7ARFLEoeLOyPKpNS0PH1Lau9F20dRI59A2gnLI2AwiYC3AqYwBl6wkG1jDps8Q5o614keeyaLdr7Ks9r45d20qZm87x2wt+sncHP3Y/lsnLis3iS1hnhGCZC0qMdW011F0vuKuLE4KPKOCdjywAcpLlE48eAe9/uMLhdZreN/E3yHISzxLxQNWR7ywycoN1RrRiX5983e+sUL0z0PaqxMptsxncT1Rcpx9CziPF76fKKggt5LsHH9JskQ1XhonifWK9Si5NY1at"
            },
            {
                "name": "http",
                "type": "port",
                "port": 80
            },
        ]
    },
    {
        "hostname": "vm86old.cd80.net",
        "services": [
            {
                "name": "ssh",
                "type": "ssh",
                "port": 22,
                "key": "AAAAB3NzaC1yc2EAAAADAQABAAABAQDcy6HBvcRtQ4zb3YlWh19IedA+MtnBPKUQ3RIbromp67K/NhGSGZM0l08MQqkXntSB5d0FKS/gwl+xIMl94H9AKtEzcV9lpxT0m+/T7dLvTDSwyZckDHiCQK8X6jNC4AMb8q6duhtLwM6F3VR2yu6VSu0m41GXrup7Jqnpw2goT9JMDaERjYMCi4C41pMvv+A8aGKZYwYtEv58jF1pE8KYJp51RFqr37lPJACEqUEO+h8IgQYfNgSKmmsfrCcvxJof1Is0iQfP53rAbjYYTA97K0F0YhtEk2h9cI4xy3T5dbVUPPsXzPceIYZeUw2MVyphS/NQtUqVyC21RvhR9QXF"
            },
            {
                "name": "ssh (alternative port)",
                "type": "ssh",
                "port": 443,
                "key": "AAAAB3NzaC1yc2EAAAADAQABAAABAQDcy6HBvcRtQ4zb3YlWh19IedA+MtnBPKUQ3RIbromp67K/NhGSGZM0l08MQqkXntSB5d0FKS/gwl+xIMl94H9AKtEzcV9lpxT0m+/T7dLvTDSwyZckDHiCQK8X6jNC4AMb8q6duhtLwM6F3VR2yu6VSu0m41GXrup7Jqnpw2goT9JMDaERjYMCi4C41pMvv+A8aGKZYwYtEv58jF1pE8KYJp51RFqr37lPJACEqUEO+h8IgQYfNgSKmmsfrCcvxJof1Is0iQfP53rAbjYYTA97K0F0YhtEk2h9cI4xy3T5dbVUPPsXzPceIYZeUw2MVyphS/NQtUqVyC21RvhR9QXF"
            },
        ]
    },
    {
        "hostname": "mmap.cd80.net",
        "services": [
            {
                "name": "ssh",
                "type": "ssh",
                "port": 22,
                "key": "AAAAB3NzaC1yc2EAAAADAQABAAABAQC4fSEu6jdKe5FEJNqsWXvOLaErOMwXTnubCnAwXFZAl7BYVUdzKIJ2eo+n8/8GEjV+2zpzB/EUTrwgGAgdG53aEBCReSx2y5zwoRukxA4BD5S32HcaJyCKTBmycEWguR7sDP360UZhTwZWw5lPCaRt2DY+mo/G20/P0QVp15y7s+B+MyObGGRsvcI5h+n/jEYOPKnnCg0denSx/WwjtPh4/IcitG82/N701Ee3F6m0CU72n8MxQ4kIBnA7OPhTriAAD4NRKDwVc90iJdsc6KstipA4GDdKWsBRHZNkzzAmoYL5hEVjSQAPAyJvbS8MTaWiMW/k+q24p4X7EUMXfcEB"
            },
            {
                "name": "http",
                "type": "port",
                "port": 80
            },
            {
                "name": "https",
                "type": "port",
                "port": 443
            },
            {
                "name": "smtp",
                "type": "port",
                "port": 25
            },
            {
                "name": "smtps",
                "type": "port",
                "port": 465
            },
            {
                "name": "imap",
                "type": "port",
                "port": 143
            },
            {
                "name": "imaps",
                "type": "port",
                "port": 993
            },
        ]
    },
    {
        "hostname": "munmap.cd80.net",
        "services": [
            {
                "name": "ssh",
                "type": "ssh",
                "port": 22,
                "key": "AAAAB3NzaC1yc2EAAAADAQABAAABAQDkv7q512ueQiJymv78Qor10no/Ib6ADvjTF/nd577hOF0U9UWe/9yUWP0dUk1mwST7RB/ZUMGElxmCcPBOwH0AHciwGPIZYZbFZporkDvi0V0FaoExZXJjg4lTsvhUXtLTFqF0ouJCGbK8YrTGNXLd045ZoaL9QHzdgtS5xahkcXuruwiieYqSaW0tb93923NqLkIjSWEdwG9pJQj6q9ljmuN090MGS0hQ05c0gWDilCgG21F+frLtHHr+U/u1Bw83H9uhscV3nhPa7WgIB07nFOvkq8qFnZEDhMnnO7fwUAQ7MBxXGBb19BKlD8HzbttTbbamgPnEfci32W7O/vnj"
            },
            {
                "name": "http",
                "type": "port",
                "port": 80
            },
            {
                "name": "https",
                "type": "port",
                "port": 443
            },
            {
                "name": "smtp",
                "type": "port",
                "port": 25
            },
            {
                "name": "git",
                "type": "port",
                "port": 9418
            },
        ]
    },
    {
        "hostname": "buzz.3on.fr",
        "services": [
            {
                "name": "ssh",
                "type": "ssh",
                "port": 1987,
                "key": "AAAAB3NzaC1yc2EAAAADAQABAAAAgQCpaQHys5Ee7KGC/VlhGdwJ92rF7SDkBarHAkSFiGsAqqnr7pVqxw2siAcrnqyZdpnAN8bp6LtBXlpiDooHFGTeXnT2WPJGTEGJPqqiZuLSJcq+2C24WRiG7LK3dvJMg+py+XoHz0T3YMXIGMmhA8HCZy6e305SOUe7APSqZuxJHw=="
            },
            {
                "name": "http",
                "type": "port",
                "port": 80
            },
            {
                "name": "https",
                "type": "port",
                "port": 443
            },
        ]
    },
]
