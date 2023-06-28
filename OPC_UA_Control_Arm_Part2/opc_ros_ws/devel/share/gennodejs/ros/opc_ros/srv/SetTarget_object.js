// Auto-generated. Do not edit!

// (in-package opc_ros.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class SetTarget_objectRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.color_name = null;
    }
    else {
      if (initObj.hasOwnProperty('color_name')) {
        this.color_name = initObj.color_name
      }
      else {
        this.color_name = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SetTarget_objectRequest
    // Serialize message field [color_name]
    bufferOffset = _serializer.string(obj.color_name, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SetTarget_objectRequest
    let len;
    let data = new SetTarget_objectRequest(null);
    // Deserialize message field [color_name]
    data.color_name = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.color_name.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'opc_ros/SetTarget_objectRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c1ebd3bdb7f211ac2ddd328c08dba1e4';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string color_name
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SetTarget_objectRequest(null);
    if (msg.color_name !== undefined) {
      resolved.color_name = msg.color_name;
    }
    else {
      resolved.color_name = ''
    }

    return resolved;
    }
};

class SetTarget_objectResponse {
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
    // Serializes a message object of type SetTarget_objectResponse
    // Serialize message field [success]
    bufferOffset = _serializer.bool(obj.success, buffer, bufferOffset);
    // Serialize message field [message]
    bufferOffset = _serializer.string(obj.message, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SetTarget_objectResponse
    let len;
    let data = new SetTarget_objectResponse(null);
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
    return 'opc_ros/SetTarget_objectResponse';
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
    const resolved = new SetTarget_objectResponse(null);
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
  Request: SetTarget_objectRequest,
  Response: SetTarget_objectResponse,
  md5sum() { return 'b043027b67620a7221fbfd7733360ab7'; },
  datatype() { return 'opc_ros/SetTarget_object'; }
};
