import { Injectable } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';
import { RequestOptions, Headers, Response } from '@angular/http';
import { Http } from '@angular/http';
import 'rxjs/Rx';

@Injectable()
export class MyServiceService {

  url:string;

  options:{headers:Headers} = {headers : null};
  
	constructor(public http:Http) {
		this.url = "http://127.0.0.1:5000/";
	}

    public getAll(): any {
        
        return this.http.get(this.url+"/lists")
          .map((response: Response) => response.json());
    }

    public getChomageByGovName(name: string): any{
      return this.http.get(this.url+"/Chomage/?name="+name+"/",this.options)
        .map((data: Response) => data.json());
    }

    public getChomage(): any{
      console.log("c bon")
      return this.http.get(this.url+"/Chomages/",this.options)
        .map((data: Response) => data.json());
    }
}
