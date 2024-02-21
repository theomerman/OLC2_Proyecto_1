import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { MonacoEditorModule } from 'ngx-monaco-editor-v2';
import { SetTextService } from '../services/setText/set-text.service';
import { SendToServerService } from '../services/sendToServer/send-to-server.service';

@Component({
  selector: 'app-editor',
  standalone: true,
  imports: [FormsModule, MonacoEditorModule],
  templateUrl: './editor.component.html',
  styleUrl: './editor.component.css'
})
export class EditorComponent {
  editorOptions = {theme: 'vs-dark', language: 'java'};
  code: string= '';
  constructor(private reveivedData: SetTextService, private sendToServer: SendToServerService) { 
    this.reveivedData.string$.subscribe(data => {
      this.code = data;
    }); 
   }
  sendCode(): void {
    let tmp = {
      "code": this.code
    }
    this.sendToServer.sendJson(tmp);

  }

}
