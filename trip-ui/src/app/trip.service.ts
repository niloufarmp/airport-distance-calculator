import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class TripService {

  constructor(private http: HttpClient) {
  }

  computeDistance(firstAirport: string, secondAirport: string) {
    let headers_object = new HttpHeaders();
    headers_object = headers_object.append('Content-Type', 'application/json');
    headers_object = headers_object.append('Authorization', 'Basic ' + btoa('niloufar:tripadmin'));

    const httpOptions = {
      headers: headers_object
    };
    return this.http.get('http://trip-backend-env.wj8eidghpr.ca-central-1.elasticbeanstalk.com/api/airport/' +
      firstAirport + '/' + secondAirport + '/distance',
      httpOptions);
  }

  airPortsList() {
    return this.http.get('http://trip-backend-env.wj8eidghpr.ca-central-1.elasticbeanstalk.com/api/airport/list');
  }
}
