// Auto-generated. Do not edit!

// (in-package jetmax_control.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Mecanum {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.velocity = null;
      this.direction = null;
      this.angular_rate = null;
    }
    else {
      if (initObj.hasOwnProperty('velocity')) {
        this.velocity = initObj.velocity
      }
      else {
        this.velocity = 0.0;
      }
      if (initObj.hasOwnProperty('direction')) {
        this.direction = initObj.direction
      }
      else {
        this.direction = 0.0;
      }
      if (initObj.hasOwnProperty('angular_rate')) {
        this.angular_rate = initObj.angular_rate
      }
      else {
        this.angular_rate = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Mecanum
    // Serialize message field [velocity]
    bufferOffset = _serializer.float32(obj.velocity, buffer, bufferOffset);
    // Serialize message field [direction]
    bufferOffset = _serializer.float32(obj.direction, buffer, bufferOffset);
    // Serialize message field [angular_rate]
    bufferOffset = _serializer.float32(obj.angular_rate, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Mecanum
    let len;
    let data = new Mecanum(null);
    // Deserialize message field [velocity]
    data.velocity = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [direction]
    data.direction = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [angular_rate]
    data.angular_rate = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'jetmax_control/Mecanum';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'ac02d3f7aa8716c10f969453bc5f21a8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 velocity
    float32 direction
    float32 angular_rate
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Mecanum(null);
    if (msg.velocity !== undefined) {
      resolved.velocity = msg.velocity;
    }
    else {
      resolved.velocity = 0.0
    }

    if (msg.direction !== undefined) {
      resolved.direction = msg.direction;
    }
    else {
      resolved.direction = 0.0
    }

    if (msg.angular_rate !== undefined) {
      resolved.angular_rate = msg.angular_rate;
    }
    else {
      resolved.angular_rate = 0.0
    }

    return resolved;
    }
};

module.exports = Mecanum;
