// Copyright 2018 Google Inc. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS-IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

import 'core-js/es/array';
import 'core-js/es/function';
import 'core-js/es/map';
import 'core-js/es/number';
import 'core-js/es/object';
import 'core-js/es/string';
import 'core-js/es/symbol';
import 'core-js/proposals/reflect-metadata';
import 'zone.js/dist/zone';
import 'rxjs';

import {platformBrowser} from '@angular/platform-browser';

import {AppModuleNgFactory} from './app.ngfactory';


platformBrowser().bootstrapModuleFactory(AppModuleNgFactory);
