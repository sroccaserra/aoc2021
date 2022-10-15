%%
% IO Functions

get_parsed_lines(FileName, ParseFn) ->
    {ok, Device} = file:open(FileName, [read]),
    try
        parse_all_lines(Device, ParseFn)
    after
        file:close(Device)
    end.

parse_all_lines(Device, ParseFn) ->
    case io:get_line(Device, []) of
        eof  -> [];
        Line -> [ParseFn(string:trim(Line)) | parse_all_lines(Device, ParseFn)]
    end.
