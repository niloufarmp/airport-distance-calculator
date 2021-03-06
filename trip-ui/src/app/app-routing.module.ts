import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {AirportComponent} from './airport/airport.component';

const routes: Routes = [
  {
    path: '',
    component: AirportComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
