// Auto-generated. Do not edit!

// (in-package remote_control.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class ChangePositionRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.axis_name = null;
      this.change_value = null;
      this.duration = null;
    }
    else {
      if (initObj.hasOwnProperty('axis_name')) {
        this.axis_name = initObj.axis_name
      }
      else {
        this.axis_name = '';
      }
      if (initObj.hasOwnProperty('change_value')) {
        this.change_value = initObj.change_value
      }
      else {
        this.change_value = 0.0;
      }
      if (initObj.hasOwnProperty('duration')) {
        this.duration = initObj.duration
      }
      else {
        this.duration = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ChangePositionRequest
    // Serialize message field [axis_name]
    bufferOffset = _serializer.string(obj.axis_name, buffer, bufferOffset);
    // Serialize message field [change_value]
    bufferOffset = _serializer.float32(obj.change_value, buffer, bufferOffset);
    // Serialize message field [duration]
    bufferOffset = _serializer.float32(obj.duration, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ChangePositionRequest
    let len;
    let data = new ChangePositionRequest(null);
    // Deserialize message field [axis_name]
    data.axis_name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [change_value]
    data.change_value = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [duration]
    data.duration = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.axis_name.length;
    return length + 12;
  }

  static datatype() {
    // Returns string type for a service object
    return 'remote_control/ChangePositionRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '26811b883eeb4b422a9e3afbc3ae3f3f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string axis_name
    float32 change_value
    float32 duration
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ChangePositionRequest(null);
    if (msg.axis_name !== undefined) {
      resolved.axis_name = msg.axis_name;
    }
    else {
      resolved.axis_name = ''
    }

    if (msg.change_value !== undefined) {
      resolved.change_value = msg.change_value;
    }
    else {
      resolved.change_value = 0.0
    }

    if (msg.duration !== undefined) {
      resolved.duration = msg.duration;
    }
    else {
      resolved.duration = 0.0
    }

    return resolved;
    }
};

class ChangePositionResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.success = null;
      this.message = null;
    }
    else {
      if (initObj.hasOwnProperty('success')) {
        this.success = initObj.success
      }
      else {
        this.success = false;
      }
      if (initObj.hasOwnProperty('message')) {
        this.message = initObj.message
      }
      else {
        this.message = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ChangePositionResponse
    // Serialize message field [success]
    bufferOffset = _serializer.bool(obj.success, buffer, bufferOffset);
    // Serialize message field [message]
    bufferOffset = _serializer.string(obj.message, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ChangePositionResponse
    let len;
    let data = new ChangePositionResponse(null);
    // Deserialize message field [success]
    data.success = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [message]
    data.message = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.message.length;
    return length + 5;
  }

  static datatype() {
    // Returns string type for a service object
    return 'remote_control/ChangePositionResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '937c9679a518e3a18d831e57125ea522';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool success
    string message
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ChangePositionResponse(null);
    if (msg.success !== undefined) {
      resolved.success = msg.success;
    }
    else {
      resolved.success = false
    }

    if (msg.message !== undefined) {
      resolved.message = msg.message;
    }
    else {
      resolved.message = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: ChangePositionRequest,
  Response: ChangePositionResponse,
  md5sum() { return '792555415d8fe5c4e60a69456efc5174'; },
  datatype() { return 'remote_control/ChangePosition'; }
};
