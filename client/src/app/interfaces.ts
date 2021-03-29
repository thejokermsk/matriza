export interface Events {
  id?: number
  name: string
  date_events: string
}

export interface Times {
  time: string
}

export interface Data {
  id?: number
  name: string
  events: {
    event_time: {time: string}
    company: {name: string}
  }[]
}


export interface Event {
  times: Times[]
  data: Data[]
}




