import { Component, OnInit } from '@angular/core';
import { DataService } from './services/data.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'scraper';
  scraperData: any[] = [];

  constructor(private dataService: DataService) {}

  ngOnInit() {
    this.fetchData();
  }

  fetchData() {
    this.dataService.getData().subscribe((data:any[]) => {
      this.scraperData = data;
    });
  }
}
