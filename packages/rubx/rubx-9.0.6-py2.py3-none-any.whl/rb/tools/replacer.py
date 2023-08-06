#!/bin/python

from re import findall


class Metas(
    object
    ):
    def checker(
        text: str
        ) -> list:
        result, texts = [], text.replace(
            '**', ''
            ).replace(
                '__', ''
                ).replace(
                    '``',
                    ''
                    ).replace(
                        '__',
                        ''
                        )
        if (
            '**' in text
            ):
            Bold: list = findall(
                r'\*\*(.*?)\*\*',
                text
                )
        boldFromIndex: list = [
            text.index(
                i
                ) for i in Bold
            ]
        [
            (
                result.append(
                    {
                        'from_index'    :   from_index-2,
                        'length'        :   len(length),
                        'type'          :   'Bold'
                        }
                    )
                ) for from_index, length in zip(
                    boldFromIndex,
                    Bold
                    )
                ]
        if (
            '__' in text
            ):
            Italic: list = findall(
                r'\_\_(.*?)\_\_',
                text
                )
        ItalicFromIndex: list = [
            text.index(
                i
                ) for i in Italic
            ]
        [
            (
                result.append(
                    {
                        'from_index'    :   from_index-2,
                        'from_index'    :   len(length),
                        'type'          :   'Italic'
                        }
                    )
                ) for from_index , length in zip(
                    ItalicFromIndex,
                    Italic
                    )
                ]
        if (
            '``' in text
            ):
            Mono: list = findall(
                r'\`\`(.*?)\`\`',
                text
                )
        monoFromIndex: list = [
            text.index(
                i
                ) for i in Mono
            ]
        [
            text.index(
                i
                ) for i in Mono
            ]
        [
            (
                result.append(
                    {
                        'from_index'    :   from_index-2,
                        'length'        :   len(length),
                        'type'          :   'Mono'
                        }
                    )
                ) for from_index , length in zip(
                    monoFromIndex,
                    Mono
                    )
                ]
        return [
            result,
            texts
            ]

class Tags(
    object
    ):
    def checker(
        text: str,
        guids=None,
        types=None) -> list:
        (
            result,
            texts
            ) = [], text.replace(
            '@',
            ''
            )
        Tags: list = findall(
            r'\@(.*?)\@',
            text
            )
        tagFromIndex: list = [
            text.index(
                i
                ) for i in Tags
            ]
        [
            (
                result.append(
                    {
                        'type'                      :   'MentionText',
                        'mention_text_object_guid'  :   guid,
                        'from_index'                :   from_index-1,
                        'length'                    :   len(
                            length
                            ),
                        'mention_text_object_type': mode
                        }
                    )
                )
            for from_index,
            length,
            guid,
            mode in zip(
                tagFromIndex,
                Tags,
                guids,
                types
                )
            ]
        return [
            result,
            texts
            ]