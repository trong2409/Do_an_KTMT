// Auto-generated. Do not edit!

// (in-package color_sorting.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class SetTargetRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.color_name = null;
      this.is_enable = null;
    }
    else {
      if (initObj.hasOwnProperty('color_name')) {
        this.color_name = initObj.color_name
      }
      else {
        this.color_name = '';
      }
      if (initObj.hasOwnProperty('is_enable')) {
        this.is_enable = initObj.is_enable
      }
      else {
        this.is_enable = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SetTargetRequest
    // Serialize message field [color_name]
    bufferOffset = _serializer.string(obj.color_name, buffer, bufferOffset);
    // Serialize message field [is_enable]
    bufferOffset = _serializer.bool(obj.is_enable, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SetTargetRequest
    let len;
    let data = new SetTargetRequest(null);
    // Deserialize message field [color_name]
    data.color_name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [is_enable]
    data.is_enable = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.color_name.length;
    return length + 5;
  }

  static datatype() {
    // Returns string type for a service object
    return 'color_sorting/SetTargetRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'e558a1453be40987777ec3a3895b6b5b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string color_name
    bool is_enable
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SetTargetRequest(null);
    if (msg.color_name !== undefined) {
      resolved.color_name = msg.color_name;
    }
    else {
      resolved.color_name = ''
    }

    if (msg.is_enable !== undefined) {
      resolved.is_enable = msg.is_enable;
    }
    else {
      resolved.is_enable = false
    }

    return resolved;
    }
};

class SetTargetResponse {
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
    // Serializes a message object of type SetTargetResponse
    // Serialize message field [success]
    bufferOffset = _serializer.bool(obj.success, buffer, bufferOffset);
    // Serialize message field [message]
    bufferOffset = _serializer.string(obj.message, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SetTargetResponse
    let len;
    let data = new SetTargetResponse(null);
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
    return 'color_sorting/SetTargetResponse';
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
    const resolved = new SetTargetResponse(null);
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
  Request: SetTargetRequest,
  Response: SetTargetResponse,
  md5sum() { return 'd59dc51bea53a4877185283f71dbf83c'; },
  datatype() { return 'color_sorting/SetTarget'; }
};
