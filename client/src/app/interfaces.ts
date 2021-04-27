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
    event_time: string
    company: string
  }[]
}


export interface Event {
  title: string
  times: Times[]
  data: Data[]
}




