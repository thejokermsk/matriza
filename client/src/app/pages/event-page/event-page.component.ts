import { Component, OnDestroy, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';
import { Event } from 'src/app/interfaces';
import { EventService } from 'src/app/services/event.service';

@Component({
  selector: 'app-event-page',
  templateUrl: './event-page.component.html',
  styleUrls: ['./event-page.component.scss']
})
export class EventPageComponent implements OnInit, OnDestroy {

  constructor(
    private route: ActivatedRoute,
    private eventService: EventService
  ) { }

  oSub: Subscription

  public event: Event = null

  ngOnInit(): void {
    const id = this.route.snapshot.paramMap.get('id');

    this.oSub = this.eventService.get(+id).subscribe(callback => {
      this.event = callback


      console.log(callback);

    })
  }

  ngOnDestroy(): void {
    if (this.oSub) this.oSub.unsubscribe()
  }
}
