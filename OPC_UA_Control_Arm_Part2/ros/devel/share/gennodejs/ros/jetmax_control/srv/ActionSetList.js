// Auto-generated. Do not edit!

// (in-package jetmax_control.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class ActionSetListRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ActionSetListRequest
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ActionSetListRequest
    let len;
    let data = new ActionSetListRequest(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'jetmax_control/ActionSetListRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ActionSetListRequest(null);
    return resolved;
    }
};

class ActionSetListResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.action_sets = null;
    }
    else {
      if (initObj.hasOwnProperty('action_sets')) {
        this.action_sets = initObj.action_sets
      }
      else {
        this.action_sets = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ActionSetListResponse
    // Serialize message field [action_sets]
    bufferOffset = _arraySerializer.string(obj.action_sets, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ActionSetListResponse
    let len;
    let data = new ActionSetListResponse(null);
    // Deserialize message field [action_sets]
    data.action_sets = _arrayDeserializer.string(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    object.action_sets.forEach((val) => {
      length += 4 + val.length;
    });
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'jetmax_control/ActionSetListResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'eef2f65442e5649b9b3489933fa21e88';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string[] action_sets
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ActionSetListResponse(null);
    if (msg.action_sets !== undefined) {
      resolved.action_sets = msg.action_sets;
    }
    else {
      resolved.action_sets = []
    }

    return resolved;
    }
};

module.exports = {
  Request: ActionSetListRequest,
  Response: ActionSetListResponse,
  md5sum() { return 'eef2f65442e5649b9b3489933fa21e88'; },
  datatype() { return 'jetmax_control/ActionSetList'; }
};
