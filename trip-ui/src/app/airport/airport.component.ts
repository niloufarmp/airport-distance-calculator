import {Component, OnInit} from '@angular/core';
import {TripService} from '../trip.service';
import {NgForm} from '@angular/forms';

@Component({
  selector: 'app-airport',
  templateUrl: './airport.component.html',
  styleUrls: ['./airport.component.css']
})
export class AirportComponent implements OnInit {

  computeDistanceResp$: Object;
  airports$: Object;
  FirstAirport: string;
  SecondAirport: string;
  error: string;
  hasError: boolean;

  constructor(private trip: TripService) {
  }

  ngOnInit() {
    this.trip.airPortsList().subscribe(
      trip => this.airports$ = trip
    );
    this.FirstAirport = 'YHZ';
    this.SecondAirport = 'AAA';
  }

  submit_form(form: NgForm): void {
    console.log('submited!', form.value);
    if (form.value.FirstAirport !== form.value.SecondAirport) {
      this.hasError = false;
      this.trip.computeDistance(form.value.FirstAirport, form.value.SecondAirport).subscribe(
        trip => this.computeDistanceResp$ = trip
      );
    } else {
      this.hasError = true;
      this.error = 'Please choose different airports';
    }
  }
}
