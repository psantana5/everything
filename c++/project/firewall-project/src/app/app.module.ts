import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MenuComponent } from './components/menu/menu.component';
import { RuleManagementComponent } from './components/rule-management/rule-management.component';
import { TrafficMonitoringComponent } from './components/traffic-monitoring/traffic-monitoring.component';
import { LoggingComponent } from './components/logging/logging.component';

@NgModule({
  declarations: [
    AppComponent,
    MenuComponent,
    RuleManagementComponent,
    TrafficMonitoringComponent,
    LoggingComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
