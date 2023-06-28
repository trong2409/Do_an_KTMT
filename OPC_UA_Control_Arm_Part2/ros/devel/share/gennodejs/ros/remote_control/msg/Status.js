// Auto-generated. Do not edit!

// (in-package remote_control.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Status {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.x = null;
      this.y = null;
      this.z = null;
      this.id1 = null;
      this.id2 = null;
      this.id3 = null;
      this.id4 = null;
      this.pwm1 = null;
      this.motor1 = null;
      this.motor2 = null;
    }
    else {
      if (initObj.hasOwnProperty('x')) {
        this.x = initObj.x
      }
      else {
        this.x = 0;
      }
      if (initObj.hasOwnProperty('y')) {
        this.y = initObj.y
      }
      else {
        this.y = 0;
      }
      if (initObj.hasOwnProperty('z')) {
        this.z = initObj.z
      }
      else {
        this.z = 0;
      }
      if (initObj.hasOwnProperty('id1')) {
        this.id1 = initObj.id1
      }
      else {
        this.id1 = 0;
      }
      if (initObj.hasOwnProperty('id2')) {
        this.id2 = initObj.id2
      }
      else {
        this.id2 = 0;
      }
      if (initObj.hasOwnProperty('id3')) {
        this.id3 = initObj.id3
      }
      else {
        this.id3 = 0;
      }
      if (initObj.hasOwnProperty('id4')) {
        this.id4 = initObj.id4
      }
      else {
        this.id4 = 0;
      }
      if (initObj.hasOwnProperty('pwm1')) {
        this.pwm1 = initObj.pwm1
      }
      else {
        this.pwm1 = 0;
      }
      if (initObj.hasOwnProperty('motor1')) {
        this.motor1 = initObj.motor1
      }
      else {
        this.motor1 = 0;
      }
      if (initObj.hasOwnProperty('motor2')) {
        this.motor2 = initObj.motor2
      }
      else {
        this.motor2 = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Status
    // Serialize message field [x]
    bufferOffset = _serializer.int16(obj.x, buffer, bufferOffset);
    // Serialize message field [y]
    bufferOffset = _serializer.int16(obj.y, buffer, bufferOffset);
    // Serialize message field [z]
    bufferOffset = _serializer.int16(obj.z, buffer, bufferOffset);
    // Serialize message field [id1]
    bufferOffset = _serializer.uint16(obj.id1, buffer, bufferOffset);
    // Serialize message field [id2]
    bufferOffset = _serializer.uint16(obj.id2, buffer, bufferOffset);
    // Serialize message field [id3]
    bufferOffset = _serializer.uint16(obj.id3, buffer, bufferOffset);
    // Serialize message field [id4]
    bufferOffset = _serializer.uint16(obj.id4, buffer, bufferOffset);
    // Serialize message field [pwm1]
    bufferOffset = _serializer.uint8(obj.pwm1, buffer, bufferOffset);
    // Serialize message field [motor1]
    bufferOffset = _serializer.uint8(obj.motor1, buffer, bufferOffset);
    // Serialize message field [motor2]
    bufferOffset = _serializer.uint8(obj.motor2, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Status
    let len;
    let data = new Status(null);
    // Deserialize message field [x]
    data.x = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [y]
    data.y = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [z]
    data.z = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [id1]
    data.id1 = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [id2]
    data.id2 = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [id3]
    data.id3 = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [id4]
    data.id4 = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [pwm1]
    data.pwm1 = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [motor1]
    data.motor1 = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [motor2]
    data.motor2 = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 17;
  }

  static datatype() {
    // Returns string type for a message object
    return 'remote_control/Status';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '590d96bbbe0686d00dc0bf91b47e905e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int16 x
    int16 y
    int16 z
    uint16 id1
    uint16 id2
    uint16 id3
    uint16 id4
    uint8 pwm1
    uint8 motor1
    uint8 motor2
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Status(null);
    if (msg.x !== undefined) {
      resolved.x = msg.x;
    }
    else {
      resolved.x = 0
    }

    if (msg.y !== undefined) {
      resolved.y = msg.y;
    }
    else {
      resolved.y = 0
    }

    if (msg.z !== undefined) {
      resolved.z = msg.z;
    }
    else {
      resolved.z = 0
    }

    if (msg.id1 !== undefined) {
      resolved.id1 = msg.id1;
    }
    else {
      resolved.id1 = 0
    }

    if (msg.id2 !== undefined) {
      resolved.id2 = msg.id2;
    }
    else {
      resolved.id2 = 0
    }

    if (msg.id3 !== undefined) {
      resolved.id3 = msg.id3;
    }
    else {
      resolved.id3 = 0
    }

    if (msg.id4 !== undefined) {
      resolved.id4 = msg.id4;
    }
    else {
      resolved.id4 = 0
    }

    if (msg.pwm1 !== undefined) {
      resolved.pwm1 = msg.pwm1;
    }
    else {
      resolved.pwm1 = 0
    }

    if (msg.motor1 !== undefined) {
      resolved.motor1 = msg.motor1;
    }
    else {
      resolved.motor1 = 0
    }

    if (msg.motor2 !== undefined) {
      resolved.motor2 = msg.motor2;
    }
    else {
      resolved.motor2 = 0
    }

    return resolved;
    }
};

module.exports = Status;
