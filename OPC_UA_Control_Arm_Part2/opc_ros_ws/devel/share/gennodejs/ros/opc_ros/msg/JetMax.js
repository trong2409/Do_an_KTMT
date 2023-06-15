// Auto-generated. Do not edit!

// (in-package opc_ros.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class JetMax {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.x = null;
      this.y = null;
      this.z = null;
      this.joint1 = null;
      this.joint2 = null;
      this.joint3 = null;
      this.servo1 = null;
      this.servo2 = null;
      this.servo3 = null;
      this.pwm1 = null;
      this.pwm2 = null;
      this.sucker = null;
    }
    else {
      if (initObj.hasOwnProperty('x')) {
        this.x = initObj.x
      }
      else {
        this.x = 0.0;
      }
      if (initObj.hasOwnProperty('y')) {
        this.y = initObj.y
      }
      else {
        this.y = 0.0;
      }
      if (initObj.hasOwnProperty('z')) {
        this.z = initObj.z
      }
      else {
        this.z = 0.0;
      }
      if (initObj.hasOwnProperty('joint1')) {
        this.joint1 = initObj.joint1
      }
      else {
        this.joint1 = 0.0;
      }
      if (initObj.hasOwnProperty('joint2')) {
        this.joint2 = initObj.joint2
      }
      else {
        this.joint2 = 0.0;
      }
      if (initObj.hasOwnProperty('joint3')) {
        this.joint3 = initObj.joint3
      }
      else {
        this.joint3 = 0.0;
      }
      if (initObj.hasOwnProperty('servo1')) {
        this.servo1 = initObj.servo1
      }
      else {
        this.servo1 = 0.0;
      }
      if (initObj.hasOwnProperty('servo2')) {
        this.servo2 = initObj.servo2
      }
      else {
        this.servo2 = 0.0;
      }
      if (initObj.hasOwnProperty('servo3')) {
        this.servo3 = initObj.servo3
      }
      else {
        this.servo3 = 0.0;
      }
      if (initObj.hasOwnProperty('pwm1')) {
        this.pwm1 = initObj.pwm1
      }
      else {
        this.pwm1 = 0.0;
      }
      if (initObj.hasOwnProperty('pwm2')) {
        this.pwm2 = initObj.pwm2
      }
      else {
        this.pwm2 = 0.0;
      }
      if (initObj.hasOwnProperty('sucker')) {
        this.sucker = initObj.sucker
      }
      else {
        this.sucker = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type JetMax
    // Serialize message field [x]
    bufferOffset = _serializer.float32(obj.x, buffer, bufferOffset);
    // Serialize message field [y]
    bufferOffset = _serializer.float32(obj.y, buffer, bufferOffset);
    // Serialize message field [z]
    bufferOffset = _serializer.float32(obj.z, buffer, bufferOffset);
    // Serialize message field [joint1]
    bufferOffset = _serializer.float32(obj.joint1, buffer, bufferOffset);
    // Serialize message field [joint2]
    bufferOffset = _serializer.float32(obj.joint2, buffer, bufferOffset);
    // Serialize message field [joint3]
    bufferOffset = _serializer.float32(obj.joint3, buffer, bufferOffset);
    // Serialize message field [servo1]
    bufferOffset = _serializer.float32(obj.servo1, buffer, bufferOffset);
    // Serialize message field [servo2]
    bufferOffset = _serializer.float32(obj.servo2, buffer, bufferOffset);
    // Serialize message field [servo3]
    bufferOffset = _serializer.float32(obj.servo3, buffer, bufferOffset);
    // Serialize message field [pwm1]
    bufferOffset = _serializer.float32(obj.pwm1, buffer, bufferOffset);
    // Serialize message field [pwm2]
    bufferOffset = _serializer.float32(obj.pwm2, buffer, bufferOffset);
    // Serialize message field [sucker]
    bufferOffset = _serializer.bool(obj.sucker, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type JetMax
    let len;
    let data = new JetMax(null);
    // Deserialize message field [x]
    data.x = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [y]
    data.y = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [z]
    data.z = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [joint1]
    data.joint1 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [joint2]
    data.joint2 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [joint3]
    data.joint3 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [servo1]
    data.servo1 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [servo2]
    data.servo2 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [servo3]
    data.servo3 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [pwm1]
    data.pwm1 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [pwm2]
    data.pwm2 = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [sucker]
    data.sucker = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 45;
  }

  static datatype() {
    // Returns string type for a message object
    return 'opc_ros/JetMax';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '98e79b4f27f832f857f4f7315fd89046';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 x
    float32 y
    float32 z
    float32 joint1
    float32 joint2
    float32 joint3
    float32 servo1
    float32 servo2
    float32 servo3
    float32 pwm1
    float32 pwm2
    bool    sucker
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new JetMax(null);
    if (msg.x !== undefined) {
      resolved.x = msg.x;
    }
    else {
      resolved.x = 0.0
    }

    if (msg.y !== undefined) {
      resolved.y = msg.y;
    }
    else {
      resolved.y = 0.0
    }

    if (msg.z !== undefined) {
      resolved.z = msg.z;
    }
    else {
      resolved.z = 0.0
    }

    if (msg.joint1 !== undefined) {
      resolved.joint1 = msg.joint1;
    }
    else {
      resolved.joint1 = 0.0
    }

    if (msg.joint2 !== undefined) {
      resolved.joint2 = msg.joint2;
    }
    else {
      resolved.joint2 = 0.0
    }

    if (msg.joint3 !== undefined) {
      resolved.joint3 = msg.joint3;
    }
    else {
      resolved.joint3 = 0.0
    }

    if (msg.servo1 !== undefined) {
      resolved.servo1 = msg.servo1;
    }
    else {
      resolved.servo1 = 0.0
    }

    if (msg.servo2 !== undefined) {
      resolved.servo2 = msg.servo2;
    }
    else {
      resolved.servo2 = 0.0
    }

    if (msg.servo3 !== undefined) {
      resolved.servo3 = msg.servo3;
    }
    else {
      resolved.servo3 = 0.0
    }

    if (msg.pwm1 !== undefined) {
      resolved.pwm1 = msg.pwm1;
    }
    else {
      resolved.pwm1 = 0.0
    }

    if (msg.pwm2 !== undefined) {
      resolved.pwm2 = msg.pwm2;
    }
    else {
      resolved.pwm2 = 0.0
    }

    if (msg.sucker !== undefined) {
      resolved.sucker = msg.sucker;
    }
    else {
      resolved.sucker = false
    }

    return resolved;
    }
};

module.exports = JetMax;
