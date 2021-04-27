import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { Events } from 'src/app/interfaces';
import { EventService } from 'src/app/services/event.service';

@Component({
  selector: 'app-index-page',
  templateUrl: './index-page.component.html',
  styleUrls: ['./index-page.component.scss']
})
export class IndexPageComponent implements OnInit, OnDestroy {

  constructor(
    private eventService: EventService,
  ) { }

  private oSub: Subscription

  public events: Events[] = []

  displayedColumns: string[] = ['name', 'date_event', 'actions', ];

  ngOnInit(): void {
    const params = {}
    this.oSub = this.eventService.getList(params).subscribe(callback => {
      this.events = callback
    })
  }

  ngOnDestroy(): void {
    if (this.oSub) this.oSub.unsubscribe()
  }
}
