import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { MenuComponent } from './components/menu/menu.component';
import { RuleManagementComponent } from './components/rule-management/rule-management.component';
import { TrafficMonitoringComponent } from './components/traffic-monitoring/traffic-monitoring.component';
import { LoggingComponent } from './components/logging/logging.component';

const routes: Routes = [
  { path: '', component: MenuComponent },
  { path: 'rule-management', component: RuleManagementComponent },
  { path: 'traffic-monitoring', component: TrafficMonitoringComponent },
  { path: 'logging', component: LoggingComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
