import { Component } from '@angular/core';

interface FirewallRule {
  ipAddress: string;
  allow: boolean;
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  firewallRules: FirewallRule[] = [];
  showTrafficMenu = false;

  addFirewallRule() {
    const ipAddress = prompt('Enter IP address:');
    const choice = prompt('Allow or block? (a/b):');
    const allow = choice === 'a' || choice === 'A';
    this.firewallRules.push({ ipAddress, allow });
    console.log('Firewall rule added successfully.');
  }

  removeFirewallRule() {
    const ipAddress = prompt('Enter IP address to remove:');
    const index = this.firewallRules.findIndex(rule => rule.ipAddress === ipAddress);
    if (index !== -1) {
      this.firewallRules.splice(index, 1);
      console.log('Firewall rule removed successfully.');
    } else {
      console.log('Firewall rule not found for the given IP address.');
    }
  }

  clearFirewallRules() {
    this.firewallRules = [];
    console.log('All firewall rules cleared.');
  }

  printFirewallRules() {
    console.log('Firewall Rules:');
    this.firewallRules.forEach(rule => {
      const action = rule.allow ? 'Allow' : 'Block';
      console.log(`IP: ${rule.ipAddress}  Action: ${action}`);
    });
  }

  countFirewallRules() {
    console.log(`Total firewall rules: ${this.firewallRules.length}`);
  }

  searchFirewallRule() {
    const ipAddress = prompt('Enter IP address to search:');
    const rule = this.firewallRules.find(rule => rule.ipAddress === ipAddress);
    if (rule) {
      const action = rule.allow ? 'Allow' : 'Block';
      console.log(`Firewall rule found for IP: ${rule.ipAddress}  Action: ${action}`);
    } else {
      console.log('No firewall rule found for the given IP address.');
    }
  }

  toggleTrafficMenu() {
    this.showTrafficMenu = !this.showTrafficMenu;
  }

  blockAllTraffic() {
    this.firewallRules = [{ ipAddress: '0.0.0.0', allow: false }];
    console.log('All traffic blocked. Firewall rules updated.');
  }

  allowAllTraffic() {
    this.firewallRules = [{ ipAddress: '0.0.0.0', allow: true }];
    console.log('All traffic allowed. Firewall rules updated.');
  }

  blockTrafficByRange() {
    const startIp = prompt('Enter starting IP address:');
    const endIp = prompt('Enter ending IP address:');
    this.firewallRules.push({ ipAddress: startIp, allow: false });
    this.firewallRules.push({ ipAddress: endIp, allow: false });
    console.log(`Blocked traffic from IP range ${startIp} to ${endIp}. Firewall rules updated.`);
  }

  allowTrafficByRange() {
    const startIp = prompt('Enter starting IP address:');
    const endIp = prompt('Enter ending IP address:');
    this.firewallRules.push({ ipAddress: startIp, allow: true });
    this.firewallRules.push({ ipAddress: endIp, allow: true });
    console.log(`Allowed traffic from IP range ${startIp} to ${endIp}. Firewall rules updated.`);
  }

  blockTrafficByProtocol() {
    const protocol = prompt('Enter protocol to block:');
    this.firewallRules.push({ ipAddress: protocol, allow: false });
    console.log(`Blocked traffic for protocol ${protocol}. Firewall rules updated.`);
  }

  allowTrafficByProtocol() {
    const protocol = prompt('Enter protocol to allow:');
    this.firewallRules.push({ ipAddress: protocol, allow: true });
    console.log(`Allowed traffic for protocol ${protocol}. Firewall rules updated.`);
  }

  blockTrafficByPort() {
    const port = prompt('Enter port to block:');
    this.firewallRules.push({ ipAddress: port, allow: false });
    console.log(`Blocked traffic for port ${port}. Firewall rules updated.`);
  }

  allowTrafficByPort() {
    const port = prompt('Enter port to allow:');
    this.firewallRules.push({ ipAddress: port, allow: true });
    console.log(`Allowed traffic for port ${port}. Firewall rules updated.`);
  }

  exitApp() {
    console.log('Exiting...');
  }
}
