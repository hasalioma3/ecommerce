import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { Ng2CarouselamosModule } from 'ng2-carouselamos';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

import { AppComponent } from './app.component';
import { CarouselPauseComponent } from './carousel-pause/carousel-pause.component';

@NgModule({
  declarations: [
    AppComponent,
    CarouselPauseComponent
  ],
  imports: [
    BrowserModule,
    Ng2CarouselamosModule,
    NgbModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
