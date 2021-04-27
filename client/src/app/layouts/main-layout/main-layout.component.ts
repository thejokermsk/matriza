import { Component, OnDestroy, OnInit } from '@angular/core';
import { EventService } from 'src/app/services/event.service';
import * as moment from 'moment-timezone';

@Component({
  selector: 'app-main-layout',
  templateUrl: './main-layout.component.html',
  styleUrls: ['./main-layout.component.scss']
})

export class MainLayoutComponent implements OnInit, OnDestroy {

  constructor(
    public eventService: EventService
  ) { }

  private getDate() {
    return moment(new Date())
      .tz('Asia/Tashkent')
  }

  private interval;

  public time = this.getDate().format('HH:mm')

  ngOnInit(): void {
    this.interval = setInterval(() => {
      this.time = this.getDate().format('HH:mm')
    }, 5000)
  }

  ngOnDestroy(): void {
    clearInterval(this.interval)
  }
}
