import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  // private dataClient = 'nifty50'
  
  constructor(private http: HttpClient) { }
  private apiUrl = 'http://127.0.0.1:5000/api/';

  getData(): Observable<any> {
    return this.http.get<any>(this.apiUrl+'/getData');
  }
}
