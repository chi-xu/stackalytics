# Copyright (c) 2013 Mirantis Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

default_data = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "required": ["users", "releases", "companies", "repos", "project_types"],
    "properties": {
        "users": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "launchpad_id": {
                        "type": "string",
                        "pattern": "^[a-z\\d\\.\\+-]+$"
                    },
                    "github_id": {
                        "type": "string"
                    },
                    "zanata_id": {
                        "type": "string"
                    },
                    "user_name": {
                        "type": "string"
                    },
                    "emails": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "pattern": ("^[a-zA-Z\\d_\\.\\+-]+@"
                                        "([a-z\\d\\.-]+\\.)"
                                        "*(([a-z]+)|\\(none\\))$")
                        },
                        "minItems": 1
                    },
                    "companies": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "company_name": {
                                    "type": "string"
                                },
                                "end_date": {
                                    "$ref": "#/definitions/date_format"
                                }
                            },
                            "required": ["company_name", "end_date"],
                            "additionalProperties": False
                        },
                        "minItems": 1
                    }
                },
                "required": ["user_name", "emails"],
                "additionalProperties": False
            }
        },
        "releases": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "release_name": {
                        "type": "string"
                    },
                    "project": {
                        "type": "string"
                    },
                    "end_date": {
                        "$ref": "#/definitions/date_format"
                    },
                    "refs": {
                        "type": "object"
                    }
                },
                "required": ["release_name", "end_date"],
                "additionalProperties": False
            }
        },
        "repos": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "uri": {
                        "type": "string"
                    },
                    "organization": {
                        "type": "string"
                    },
                    "module": {
                        "type": "string"
                    },
                    "releases": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "branch": {
                                    "type": "string"
                                },
                                "tag_from": {
                                    "type": "string"
                                },
                                "tag_to": {
                                    "type": "string"
                                },
                                "release_name": {
                                    "type": "string"
                                }
                            },
                            "required": ["tag_from", "tag_to", "release_name"]
                        }
                    },
                    "aliases": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "default_branch": {
                        "type": "string"
                    }
                },
                "required": ["uri", "module", "organization"],
                "additionalProperties": False
            }
        },
        "companies": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "company_name": {
                        "type": "string"
                    },
                    "domains": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "pattern": "^[a-z\\d\\.-]*$"
                        }
                    },
                    "aliases": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    }
                },
                "required": ["company_name", "domains"],
                "additionalProperties": False
            }
        },
        "project_sources": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "organization": {
                        "type": "string"
                    },
                    "uri": {
                        "type": "string"
                    },
                    "git_base_uri": {
                        "type": "string"
                    },
                    "ssh_key_filename": {
                        "type": "string"
                    },
                    "ssh_username": {
                        "type": "string"
                    },
                    "exclude": {
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "default_branch": {
                        "type": "string"
                    },
                    "module_group_id": {
                        "type": "string"
                    },
                    "pattern": {
                        "type": "string"
                    }
                },
                "required": ["organization"],
                "additionalProperties": False
            }
        },
        "module_groups": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "module_group_name": {
                        "type": "string",
                        "pattern": "^[\\w-]+$"
                    },
                    "modules": {
                        "type": ["array"],
                        "items": {
                            "type": "string"
                        }
                    }
                },
                "required": ["module_group_name", "modules"],
                "additionalProperties": False
            }
        },
        "mail_lists": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "member_lists": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "project_types": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "string",
                        "pattern": "^[\\w:-]+$"
                    },
                    "child": {
                        "type": "boolean"
                    },
                    "title": {
                        "type": "string"
                    },
                    "modules": {
                        "type": ["array"],
                        "items": {
                            "type": "string",
                            "pattern": "^[\\w:-]+$"
                        }
                    }
                },
                "required": ["id", "title", "modules"],
                "additionalProperties": False
            }
        }
    },
    "definitions": {
        "date_format": {
            "type": ["string", "null"],
            "pattern": ("^20\\d{2}-(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|"
                        "Nov|Dec)-[0-3]\\d$")
        }
    }
}
