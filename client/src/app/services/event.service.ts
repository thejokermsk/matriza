import { HttpClient, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Event, Events } from '../interfaces';

@Injectable({
  providedIn: 'root'
})
export class EventService {

  constructor(
    private http: HttpClient
  ) { }

  public getList(params: {date?: string}): Observable<Events[]> {
    return this.http.get<Events[]>('/api/events', {
      params: new HttpParams({
        fromObject: params
      })
    })
  }

  public get(id: number): Observable<Event> {
    return this.http.get<Event>(`/api/events/detail/${id}`)
  }



}
