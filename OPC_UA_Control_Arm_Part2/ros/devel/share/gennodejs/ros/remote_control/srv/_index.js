
"use strict";

let GoHome = require('./GoHome.js')
let ChangePosition = require('./ChangePosition.js')
let SetPosition = require('./SetPosition.js')
let SetChuck = require('./SetChuck.js')
let SetServo = require('./SetServo.js')
let SetPWMServo = require('./SetPWMServo.js')

module.exports = {
  GoHome: GoHome,
  ChangePosition: ChangePosition,
  SetPosition: SetPosition,
  SetChuck: SetChuck,
  SetServo: SetServo,
  SetPWMServo: SetPWMServo,
};
