import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class SendToServerService {
// send json to api
  constructor() { }
  sendJson(json: any): void {
    const xhr = new XMLHttpRequest();
    xhr.open('POST', 'http://localhost:5000/sendCode', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify(json));
  }
}
