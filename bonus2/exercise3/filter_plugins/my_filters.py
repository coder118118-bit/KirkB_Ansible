import re


def arp_dict(output):
    arp_dict = {}
    output = output.strip()
    for line in output.splitlines():
        if re.search(r".*Address.*Interfaces$", line, flags=re.M):
            continue
        ip_address = line.split()[1]
        mac_address = line.split()[3]
        arp_dict[ip_address] = mac_address

    return arp_dict


class FilterModule(object):
    def filters(self):
        return{"arp_dict": arp_dict}
