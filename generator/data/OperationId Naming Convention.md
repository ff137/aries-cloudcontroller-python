# OperationId Naming Convention

In an effort to maintain consistency, clarity, and future-proofing in our APIs, we are adhering to a specific set of naming conventions for our operationIds. Following this convention will make the API easier to work with, more understandable, and more maintainable in the long term.

Our convention is based on several key principles:

1. **Consistency:** Consistent naming enables developers to predict operation names, understand their behavior, and infer the structure of the API.

2. **Clarity and Descriptiveness:** We aim to make our API as self-documenting as possible. Each operationId should clearly convey its purpose to minimize the need for external documentation.

3. **Brevity:** While clarity is paramount, we strive for brevity where possible. Long names can be burdensome, but should not be avoided at the cost of clarity.

4. **Future-proofing:** We must consider the growth of our API. OperationIds should not be overly specific or restrictive to allow for future changes and expansions.

With these principles in mind, we follow these specific rules for naming operationIds:

1. **Use Verbs to Start the Name:** OperationIds should begin with a verb that describes the action it performs, such as `create`, `get`, `delete`, `update`.

2. **Use Nouns for Resources:** After the verb, use the name of the resource being acted upon. For example, `create_connection`, `get_record`, `delete_credential_definition`.

3. **Use Singular or Plural Nouns as Appropriate:** For operations that act on one record, use the singular noun (e.g., `get_record`). For operations that act on multiple records, see if there's a way to make `get_records` (multiple) more distinguished from the singular method. To make a clear distinction, it is more effective to name the method `get_all_records`, if the methods returns everything, or `get_matching_records` if the method returns all records matching a filter. This is encouraged because methods like `get_record` and `get_records` are easy to mistake for one another, and usually the methods take very different request bodies (e.g. one record id, vs multiple filter fields).

4. **No Duplicate Names:** Each operationId should be unique, even if used in different contexts. This will avoid any confusion when an operationId is exposed without its context. For example, instead of `create_invitation` for both `ConnectionsApi` and `OutOfBandApi`, use `create_connection_invitation` and `create_oob_invitation`, respectively.

5. **Avoid Abbreviations:** As a general rule, avoid abbreviations unless they are widely understood (like `conn` for `connection`), and unless the method is _very_ long. Long names are preferable to uncertainty. For instance, `get_created_cred_defs` should be `get_created_credential_definitions`.

Please note that while we aim to stick to these conventions as closely as possible, there may be exceptions in cases where strict adherence would compromise clarity or practicality. In such cases, the overall goal should always be to maximize the readability and usability of the API.

Remember, the purpose of these conventions is to make our API easier to work with and understand. A little effort in adhering to these conventions now will save time and reduce errors in the future. Let's build a better API together!
